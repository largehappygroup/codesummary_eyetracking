public class FileSaver {
    public void saveToFile( File f ) {
        try {
            FileOutputStream file = new FileOutputStream( f );
            saveToFile( file );
            file.close();
        } catch ( FileNotFoundException e ) {
            e.printStackTrace();
        } catch ( IOException e ) {
            e.printStackTrace();
        }
    }
}