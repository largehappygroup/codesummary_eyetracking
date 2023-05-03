public class ContainerOpener {
    public boolean openNewContainerWindow( String containerName, String containerDescription ){
        //if name is blank, disable use default option
        NewContainerImportWindow window;
        if( containerName.equals( "" )){
            window = new NewContainerImportWindow();
        }
        else{
            window = new NewContainerImportWindow( containerName,containerDescription );
        }
        window.setParent( OrganiserView.this );
        try{
            window.doModal();
        }
        catch( InterruptedException ie ){
            ie.printStackTrace( System.err );
        }
        if( doImport ){
            importer.setContainerName( window.getName() );
            importer.setContainerDescription( window.getDescription() );
        }
        return doImport;
    }
}