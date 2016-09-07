import org.json.*;
import java.io.*;
import java.lang.*;

public class AddParses {
	private CoreNLPInterface corenlpInterface = new CoreNLPInterface();

	private void processArticle(String title) {
		try {
			System.out.println(title);

			JSONObject json = ArticleRepository.readArticle(title);
			String articleText = (String) json.get("plaintext");
			json.put("corenlp_xml", corenlpInterface.getXML(articleText));
			ArticleRepository.writeArticle(title, json);
		} catch (IOException e) {
			System.out.println("Failed: " + title);
			System.out.println(e);
		}
	}

	public void run(String[] args) {
		corenlpInterface.setup();

		for (String title : args) {
			processArticle(title);
		}
	}

	public static void main(String[] args) {
		new AddParses().run(args);
	}
}
