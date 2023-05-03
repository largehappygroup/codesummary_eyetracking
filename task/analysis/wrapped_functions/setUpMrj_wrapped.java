public class Belvedere4 {
    private static String mrjVersion;
    private static double mrjMajorVersion;

    private void setUpMrj() {
        mrjVersion = System.getProperty("mrj.version");

        if (mrjVersion == null)
            return;

        try {
            mrjMajorVersion = Double.valueOf(mrjVersion.substring(0, 3)).doubleValue();
        } catch (Exception e) {
            mrjMajorVersion = 0;
        }
    }
}