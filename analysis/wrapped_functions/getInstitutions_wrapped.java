public class InstitutionManager {
    
    private Collection iInstitutions;
    private Logger logger;
    
    public InstitutionManager() {
        this.logger = new Logger(); //Assuming Logger is a pre-defined class
    }
    
    public Collection getInstitutions() {
        try {
            if ( iInstitutions == null ) {
                refreshInstitutions();
                logger.debug( "Institutions were null while getting them. Attempting to refresh." );
            }
            return iInstitutions;
        }
        catch ( Exception e ) {
            logger.warn( e.getMessage(), e );
            return Collections.EMPTY_LIST;
        }
    }
    
    private void refreshInstitutions() {
        //Implementation for refreshing institutions goes here
    }
}