public class MoveRFTest {
    public void testMoveRFWithNullContainer() throws CoreException {
        IRodinFile rfSource = createRodinFile( "/P/X.test" );
        try {
            rfSource.move( null, null, null, false, null );
        } catch ( IllegalArgumentException iae ) {
            return;
        }
        assertTrue( "Should not be able to move a rf to a null container", false );
    }
}