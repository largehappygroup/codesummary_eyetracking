import java.io.*;

public class FieldClearer {
    public void clearFieldersFromField() {
        // clear all fielders from field
        for ( int i = 0; i < boardXDimension; i++ ) {
            for ( int j = 0; j < boardYDimension; j++ ) {
                for ( int a = 0; a < boardZDimension; a++ ) {
                    cricketFieldPositions[ i ][ j ][ a ] = 0;
                }
            }
        }
    }
}