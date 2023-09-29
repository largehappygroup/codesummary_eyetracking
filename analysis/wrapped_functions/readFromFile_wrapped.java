public class FileHandler {
	
	private String credentials;
	private String username;
	private String password;
	
	public FileHandler(String credentials) {
		this.credentials = credentials;
	}
	
	private void readFromFile() {
	    try {
	        FileReader fr = new FileReader( this.credentials );
	        BufferedReader br = new BufferedReader( fr );
	        this.username = br.readLine();
	        this.password = br.readLine();
	        br.close();
	        fr.close();
	    }
	    catch ( Exception e ) {
	        this.username = "";
	        this.password = "";
	    }
	}
}