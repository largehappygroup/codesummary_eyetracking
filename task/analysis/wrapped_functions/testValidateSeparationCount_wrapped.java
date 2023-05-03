public class LinearDimensionTest {
    public void testValidateSeparationCount() {
        try {
            LinearDimension.validateSeparationCount( 0 );
            fail();
        } catch ( IllegalArgumentException ex ) {
            // ok
        }
        try {
            LinearDimension.validateSeparationCount( -2 );
            fail();
        } catch ( IllegalArgumentException ex ) {
            // ok
        }
        LinearDimension.validateSeparationCount( 1 );
        LinearDimension.validateSeparationCount( 2988 );
    } 
}