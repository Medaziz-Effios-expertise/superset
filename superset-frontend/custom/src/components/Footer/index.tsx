import React from "react";
import { t } from '@superset-ui/core';

const legal = t('Legal Notices');
const rgpd = t('GDPR Notices');

const Footer = () => {
  return (
    <footer style={{ position: 'absolute', bottom: 0, width: '100%', height: '40px', backgroundColor: '#FCFCFC', display: 'flex', justifyContent: 'center', alignItems: 'center', padding: '0 20px' }}>
      <div style={{ display: 'flex', alignItems: 'center' }}>
        <div style={{ display: 'flex', flexDirection: 'row' }}>
          <a href="/static/custom/legal.html" style={{ margin: '0 10px', color: '#666', textDecoration: 'none', fontWeight: 'bold', fontSize: '18px' }}>{legal}</a>
          <a href="/static/custom/rgpd.html" style={{ margin: '0 10px', color: '#666', textDecoration: 'none', fontWeight: 'bold', fontSize: '18px' }}>{rgpd}</a>
        </div>
      </div>
    </footer>

  );
};

export default Footer;
