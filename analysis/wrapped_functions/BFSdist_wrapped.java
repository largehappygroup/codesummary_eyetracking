public class BFSDistClass {
    public void BFSdist(Node n, Vector ToDo, int[] indirConn) {
        Node n2 = null;
        for (Enumeration es = n.adjEdges.elements(); es.hasMoreElements();) {
            n2 = n.adjNode((Edge) es.nextElement());
            if (n2.dist < 0) {
                n2.dist = n.dist + 1;
                indirConn[n2.dist]++;
     
                // important add adds to the end of the list
                ToDo.add(n2);
            }
        }
        if (!ToDo.isEmpty()) {
            n2 = (Node) ToDo.remove(0);
            BFSdist(n2, ToDo, indirConn);
        }
    }
}