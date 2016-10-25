from src.prototype.lib import flags
from src.prototype.lib import mapper
from src.prototype.lib import article_set

def main():
    flags.add_argument('--articles_per_job', type=int, required=True)
    flags.make_parser(description='TODO')
    # TODO: add max_jobs
    args = flags.parse_args()

    art_set = article_set.ArticleSet()

    def make_commandline(articles_slice):
        return ['prototype/parse/parse'] + articles_slice

    mapper.launch_in_slices(
        'add-parses',
        art_set.article_names,
        args.articles_per_job,
        make_commandline,
        slice_to_walltime=(lambda s: "01:00:00"),
        cores=2,
        ram='9gb'
    )

if __name__ == '__main__':
    main()