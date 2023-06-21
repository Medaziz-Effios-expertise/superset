import { t } from '@superset-ui/core';
import React from 'react';

const Footer = () => {
  const M_legales = t('Mentions Légales');
  const M_rgpd = t('Mentions RGPD');

  const footerStyle: React.CSSProperties = {
    position: 'absolute',
    bottom: 0,
    width: '100%',
    height: '40px',
    backgroundColor: '#FCFCFC',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    padding: '0 20px',
  };

  const linkStyle: React.CSSProperties = {
    margin: '0 10px',
    color: '#666',
    textDecoration: 'none',
    fontWeight: 'bold',
    fontSize: '18px',
  };

  return (
    <footer style={footerStyle}>
      <div style={{ display: 'flex', alignItems: 'center' }}>
        <div style={{ display: 'flex', flexDirection: 'row' }}>
          <a href="/static/custom/legal.html" style={linkStyle}>
            {M_legales}
          </a>
          <a href="/static/custom/rgpd.html" style={linkStyle}>
            {M_rgpd}
          </a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
