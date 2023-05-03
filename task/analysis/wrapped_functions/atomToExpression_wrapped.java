public class AtomToExpressionParser {
    private static String atomToExpression( Atom atom, String name ) {
        String expr = name + " = ";
		
        if ( atom instanceof BooleanAtom ) {
            BooleanAtom booleanAtom = ( BooleanAtom ) atom;
            try {
                if( booleanAtom.getBooleanValue() )
                    expr += "'T'";
                else
                    expr += "'F'";
            } catch ( InvalidStateException e ) {
                throw new Error( "Thing in invalid boolean state" );
            }
        }		
        else if ( atom instanceof TextAtom )
            expr += "'" + atom.getValue() + "'";
        else
            expr += atom.getValue();

        return expr;
    }
}