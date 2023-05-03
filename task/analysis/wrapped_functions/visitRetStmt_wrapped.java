public class RetStmtVisitor {
    
    public void visitRetStmt( RetStmt stmt ) {
        Set targets = new LinkedHashSet();
        Iterator iter = stmt.sub().paths().iterator();

        while ( iter.hasNext() ) {
            Block[] path = ( Block[]) iter.next();
            targets.add( path[ 1 ] );
        }

        targets.addAll( stmt.catchTargets() );
        verifyTargets( stmt.block(), targets );
        visitNode( stmt );
    }

    private void verifyTargets(Block block, Set targets) {
        // implementation left out for brevity
    }

    private void visitNode(RetStmt stmt) {
        // implementation left out for brevity
    }
}