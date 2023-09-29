public class UrlSetter {
    private String[] urls;
    private String illegalPostProssingMsg = "Illegal Post-Processing";

    public void setUrls( String[] theUrls ) throws IllegalStateException {
        if ( xmlProcessed )
            throw new IllegalStateException( illegalPostProssingMsg );
		
        if( theUrls != null ) {
            this.urls = new String [ theUrls.length ];
            for( int i = 0; i < theUrls.length; i++ )
                this.urls[ i ] = UrlHelper.normalize( theUrls[ i ]);
        }
        else
            this.urls = urls;
    }
}