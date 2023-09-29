public class Format {

    public Object clone() {
        Format result = new Format();

        result.datatype = datatype;
        result.datatypeID = datatypeID;
        result.respectCase = respectCase;
        result.gap = gap;
        result.missing = missing;
        result.labels = labels;
        result.labelQuotes = labelQuotes;
        result.transpose = transpose;
        result.interleave = interleave;
        result.diploid = diploid;
        result.tokens = tokens;
        result.symbols = symbols;
        result.matchChar = matchChar;

        return result;
    }
}