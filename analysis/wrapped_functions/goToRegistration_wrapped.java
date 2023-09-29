public class NavigateToRegistration {
    private void goToRegistration() {
        m_logo.setVisible( false );
        m_login.setText( "Cancel" );
        m_userLabel.setLocation( 16, 4 );
        m_username.setLocation( 16, 24 );
        m_passLabel.setLocation( 16, 52 );
        m_password.setLocation( 16, 70 );
        m_confirmPass.setVisible( true );
        m_confPassLabel.setVisible( true );
        m_male.setVisible( true );
        m_female.setVisible( true );
        this.setTitle( "Registration" );
    }
}