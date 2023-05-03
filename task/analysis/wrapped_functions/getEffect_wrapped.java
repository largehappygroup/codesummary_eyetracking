public class StatusEffectParser {
    public StatusEffect getEffect( int lock ) {
        synchronized ( m_statuses ) {
            Iterator i = m_statuses.iterator();

            while ( i.hasNext() ) {
                StatusEffect eff = ( StatusEffect )i.next();

                if (( eff == null ) || !eff.isActive() ) {
                    continue;
                }
                if ( eff.getLock() == lock ) {
                    return eff;
                }
            }
        }
        return null;
    }
}