public class ContactDialog {
    public void show( Contact contact ) {
        logger.fine( "Showing edit contact dialog for contact: " + contact );
        this.contact = contact;
        init();
        setLocationRelativeTo( Context.mainFrame );
        optionPane.setValue( JOptionPane.UNINITIALIZED_VALUE );
        panel.setContact( contact );
        panel.prepareForShow();
        setVisible( true );
    }
}