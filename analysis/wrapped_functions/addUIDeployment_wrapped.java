public class MyJavaClass {
    
    public void addUIDeployment( SandUIDeployment uidep ) {
        SandUIDeployment[] olduis = getSandUIDeployments();
        SandUIDeployment[] newuis = new SandUIDeployment[ olduis.length + 1 ];
        System.arraycopy( olduis, 0, newuis, 0, olduis.length );
        newuis[ olduis.length ] = uidep;
        setSandUIDeployments( newuis );
    } 
    
}