public class PrintFunction {
    protected void print() {
        System.out.println( "Print for " + prototype + "------------------" );
        cfg.visit( new PrintVisitor() {
            Phi phi = null;

            public void visitBlock( final Block block ) {
                phi = exprPhiAtBlock( block );
                super.visitBlock( block );
            }
            public void visitLabelStmt( final LabelStmt stmt ) {
                super.visitLabelStmt( stmt );

                if ( stmt.label().startsBlock() ) {
                    if ( phi != null ) {
                        println( phi );
                        phi = null;
                    }
                }
            }
        });
        System.out.println( "End Print ----------------------------" );
    }
}