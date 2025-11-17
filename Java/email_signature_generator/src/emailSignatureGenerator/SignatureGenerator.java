package emailSignatureGenerator;

public class SignatureGenerator {
	
	public String generateSignature(String name, String title, String company) {
		char firstLetter = Character.toUpperCase(name.charAt(0));
		
		String prefix;
		
		if (firstLetter >= 'A' && firstLetter <= 'I') {
			prefix = ">>";
		}else if (firstLetter >= 'J' && firstLetter <= 'R'){
			prefix = "--";			
		}else {
			prefix = "::";
		}
			
		return prefix + name +", " + title +" at " + company;
		
	}

	public static void main(String[] args) {
		// Building a class object
		SignatureGenerator myGenerator = new SignatureGenerator();
		
		// Calling the method and saving the result in a variable
		String QuinnSignature = myGenerator.generateSignature("Quinn Waverly", "Founder and CEO", "TechCo");
		
		System.out.println(QuinnSignature);
	}

}
