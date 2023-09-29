public class SvgDocumentLoader {
    public void documentLoadingCompleted( SVGDocumentLoaderEvent e ) {
        if ( debug ) {
            System.out.print( "Document load completed in " );
            System.out.println(( System.currentTimeMillis() - time ) + " ms" );
        }
        setSVGDocument( e.getSVGDocument(), e.getSVGDocument().getURL(), e.getSVGDocument().getTitle() );
    }
}