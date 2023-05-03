public class SecuritySetter {
    public int setSecurityMode ( int level, String authToken ) throws RemoteException {
        if ( !this.authToken.equals( authToken )){
            throw new RemoteException( "Invalid Login Token" );
        }
        ServerSettingBean.setSecureMode( "" + level );
        serverSettingBean.updateSettings();
        securityMode = level;
        return securityMode;
    }
}