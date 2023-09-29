public class MenuAdministracion {
    
    private JMenu menuAdministracion;

    public JMenu getMenuAdministracion() {
        if ( menuAdministracion == null ) {
            menuAdministracion = new JMenu();
            menuAdministracion.setText( Messages.getString( "gui.GUI.57" )); //$NON-NLS-1$
            menuAdministracion.setIcon( new ImageIcon( "data/icons/package_system.png" )); //$NON-NLS-1$
            menuAdministracion.add( getMenuItemAdminUsuarios() );
            menuAdministracion.add( getMenuItemAdminResorces() );
        }
        return menuAdministracion;
    }

    private JMenuItem getMenuItemAdminUsuarios() {
        // Implementation of the getMenuItemAdminUsuarios method
    }
    
    private JMenuItem getMenuItemAdminResorces() {
        // Implementation of the getMenuItemAdminResorces method
    }
        
}