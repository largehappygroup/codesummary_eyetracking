public class MyClass {
    public void setGenJarDir( File genJarDir,SandProject proj ) {
        proj.getAntProject().setProperty( "genJarDir", genJarDir.toString() );
        SandProject[] downstream = proj.getRequiredBy();

        for( int i=0; i < downstream.length; i++ ) {
            setGenJarDir( genJarDir, downstream[ i ]); 
        }
    }
}