public class MemberChecker {
    public boolean checkDescendantM(Member aMember, Member dMember) {
        mondrian.olap.Member monMember = ((MondrianMember) aMember).getMonMember();
        mondrian.olap.Member monDesc = ((MondrianMember) dMember).getMonMember();

        if (monDesc.isCalculatedInQuery() || monDesc.equals(monMember))
            return false;
        return monDesc.isChildOrEqualTo(monMember);
    }
}