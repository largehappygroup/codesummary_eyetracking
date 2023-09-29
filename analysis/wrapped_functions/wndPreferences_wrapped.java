public class MainWindow {
    public void wndPreferences() {
        log.entering( "MainWindow", "wndPreferences" );
        PropertiesDlg propDlg = new PropertiesDlg( this );
        propDlg.setModal( true );
        propDlg.setVisible( true );
        log.exiting( "MainWindow", "wndPreferences" );
    }
}