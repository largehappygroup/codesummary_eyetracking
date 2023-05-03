public class GenIdents {

    public JExpression genIdents() {
        TokenReference ref = getTokenReference();
        Jexpression[] init = new JExpression[ codes.length ];

        for ( int i = 0; i < codes.length; i++ ) {
            init[ i ] = new JStringLiteral( ref, codes[ i ].getIdent() );
        }
        return VKUtils.createArray( ref, CStdType.String, init );
    }
}