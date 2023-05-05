import React from "react";

export interface FooterProps {
  companyName: string;
}

const Footer: React.FC<FooterProps> = () => {
  return (
    <footer style={{ position: 'absolute', bottom: 0, width: '100%', height: '40px', backgroundColor: '#FCFCFC', display: 'flex', justifyContent: 'center', alignItems: 'center',  padding: '0 20px' }}>
  <div style={{ display: 'flex', alignItems: 'center' }}>
    <div style={{ display: 'flex', flexDirection: 'row' }}>
      <a href="/superset/legal/" style={{ margin: '0 10px', color: '#666', textDecoration: 'none', fontWeight: 'bold', fontSize: '18px' }}>mentions légales</a>
      <a href="/superset/rgpd/" style={{ margin: '0 10px', color: '#666', textDecoration: 'none', fontWeight: 'bold', fontSize: '18px' }}>mentions RGPD</a>
    </div>
  </div>
</footer>

  );
};

export default Footer;
