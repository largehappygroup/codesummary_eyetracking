public class EmailLinkChecker {
    
    public boolean isInvalidEmailLink(String textLink, String wikiFileURL) {
        return textLink.contains( ArticleLink.EMAIL_AT_SEPARATOR ) &&
            !textLink.toLowerCase( Locale.getDefault()).startsWith( "mailto:" ) && //$NON-NLS-1$
            wikiFileURL.getWikiFileName( true ).contains( ArticleLink.EMAIL_AT_SEPARATOR );
    }
    
}