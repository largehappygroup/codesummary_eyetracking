public class ServerChooserClass {

    public static void createServerChooser() {
        MainMenuBar mainMenuBar = MainMenuBar.getInstance();

        int nodeId = dbMgr.getNodeId(( String ) cbNE.getSelectedItem());

        DownloadFileChooser downloadFile = new DownloadFileChooser( nodeId, DBDataDesc.SHELF_OLT1, tfFileName, tfFileNameOnly );

        mainMenuBar.putCommand(( Object ) downloadFile );
        downloadFile.setViewId( mainMenuBar.getViewId() );
        downloadFile.setVisible( true );
    }
    
}