public class MyClass {
    private void setUpMrj() {
        Belvedere4.mrjVersion = System.getProperty( "mrj.version" );

        if ( Belvedere4.mrjVersion == null ) return;
        try {
            Belvedere4.mrjMajorVersion = Double.valueOf( Belvedere4.mrjVersion.substring( 0, 3 )).doubleValue();
        } catch ( Exception e ) {
            Belvedere4.mrjMajorVersion = 0;
        }
    }

    static class Belvedere4 {
        static String mrjVersion;
        static double mrjMajorVersion;
    }
}