from prototype.lib import mapper
from prototype.lib import article_set
from prototype.lib import wikidata
from prototype.lib import flags

def main():
    flags.add_argument('--articles_per_job', type=int)
    # flags.add_argument('--local_parallelism', type=int, default=1)
    flags.make_parser(description='TODO')
    # TODO: add max_jobs
    args = flags.parse_args()

    wikidata_endpoint = wikidata.get_default_endpoint_url()

    def make_commandline(articles_slice):
        job_command = [
            'prototype/make_training_samples/make_training_samples',
            # '--parallelism', str(args.local_parallelism),
            '--wikidata_endpoint', wikidata_endpoint,
        ]
        for article in articles_slice:
            job_command.extend(['--articles', article])
        print(job_command)
        return job_command

    def slice_to_walltime(articles_slice):
        article_count = len(articles_slice)
        walltime_estimate = round(
            # (120 * article_count / float(args.local_parallelism)) * 2 + 100
            (120 * article_count) * 2 + 100
        ) # or default: "04:00:00"
        return walltime_estimate

    art_set = article_set.ArticleSet()

    mapper.launch_in_slices(
        'make-training-samples',
        art_set.article_names,
        args.articles_per_job,
        make_commandline,
        slice_to_walltime,
        cores=2, # max(2, args.local_parallelism)
        ram='16gb'
    )

if __name__ == '__main__':
    main()
