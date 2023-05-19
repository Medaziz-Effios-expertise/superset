import React from "react";

const Footer = () => {
  return (
    <footer style={{ position: 'absolute', bottom: 0, width: '100%', height: '40px', backgroundColor: '#FCFCFC', display: 'flex', justifyContent: 'center', alignItems: 'center', padding: '0 20px' }}>
      <div style={{ display: 'flex', alignItems: 'center' }}>
        <div style={{ display: 'flex', flexDirection: 'row' }}>
          <a href="/static/custom/legal.html" style={{ margin: '0 10px', color: '#666', textDecoration: 'none', fontWeight: 'bold', fontSize: '18px' }}>mentions légales</a>
          <a href="/static/custom/rgpd.html" style={{ margin: '0 10px', color: '#666', textDecoration: 'none', fontWeight: 'bold', fontSize: '18px' }}>mentions RGPD</a>
        </div>
      </div>
    </footer>

  );
};

export default Footer;
