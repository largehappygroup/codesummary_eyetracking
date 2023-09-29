public class LaTeXDocument {
  public void appendDeclarations(LaTeXDocumentPortion pack, LaTeXDocumentPortion decl) {
    if (bContainsEndnotes) {
      pack.append("\\usepackage{endnotes}").nl();
    }
    if (bContainsFootnotes)
      convertFootnotesConfiguration(decl);
    if (bContainsEndnotes)
      convertEndnotesConfiguration(decl);
  }
}