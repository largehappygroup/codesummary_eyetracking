public class ConnectionPanel {
    
    private JPanel connectionPanel;
    private JLabel connectionRoomLabel;
    
    public JPanel getConnectionPanel() {
        if ( connectionPanel == null ) {
            connectionRoomLabel = new JLabel();
            connectionRoomLabel.setText( "Playground" );
            connectionPanel = new JPanel();
            connectionPanel.setLayout( new BoxLayout( getConnectionPanel(), BoxLayout.X_AXIS ));
            connectionPanel.add( getConnectionsButton(), null );
            connectionPanel.add( connectionRoomLabel, null );
        }
        return connectionPanel;
    }
    
    private JButton getConnectionsButton(){
        //Method implementation
    }
}