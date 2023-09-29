public class ScopePartnerLinkFinder {
    public EList getScopePartnerLinks(final EObject process) {
        TreeIterator contents = process.eAllContents();
        EList results = new BasicEList();
            
        while (contents.hasNext()) {
            EObject obj = (EObject) contents.next();
                
            if (obj instanceof Scope) {
                results.addAll(((Scope) obj).getPartnerLinks().getChildren());
            }   
        }
        return results;
    }
}