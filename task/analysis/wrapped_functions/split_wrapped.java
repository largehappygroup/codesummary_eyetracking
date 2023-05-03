public class Splitter {
    public List split(String line) {
        List result;

        if (line == null) {
            result = new ArrayList();
        } else {
            StringTokenizer tok;
            tok = new StringTokenizer(line, ",");
            result = new ArrayList(tok.countTokens());

            while (tok.hasMoreTokens()) {
                result.add(tok.nextToken());
            }
        }
        return result;
    }
}