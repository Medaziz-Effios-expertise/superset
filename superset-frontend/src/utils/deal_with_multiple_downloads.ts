import {SyntheticEvent} from 'react';
import domToImage from 'dom-to-image-more';
import {t} from '@superset-ui/core';
import {addWarningToast} from 'src/components/MessageToasts/actions';


/**
 * Create an event handler for turning multiple elements into a single image
 *
 * @param selectors an array of css selectors of the parent elements which should be turned into image
 * @param description name or a short description of what is being printed.
 *   Value will be normalized, and a date as well as a file extension will be added.
 * @returns event handler
 */
const GRAY_BACKGROUND_COLOR = '#F5F5F5';
export default function downloadMultipleAsImage(
  selectors: string[],
  description: string,
) {
  return (event: SyntheticEvent) => {
    const elementsToPrint = selectors.map(selector =>
      event.currentTarget.closest(selector),
    );

    const filteredElements = elementsToPrint.filter(
      element => element !== null,
    );

    if (filteredElements.length === 0) {
      return addWarningToast(
        t('Image download failed, please refresh and try again.'),
      );
    }

    const promises = filteredElements.map(elementToPrint =>
      domToImage.toJpeg(elementToPrint, {
        quality: 0.95,
        bgcolor: GRAY_BACKGROUND_COLOR,
        filter: node => {
          if (typeof node.className === 'string') {
            return (
              node.className !== 'mapboxgl-control-container' &&
              !node.className.includes('ant-dropdown')
            );
          }
          return true;
        },
      }),
    );

    Promise.all(promises)
      .then(dataUrls => {
        const canvas = document.createElement('canvas');
        const width = Math.max(...filteredElements.map(e => e.offsetWidth));
        const height = filteredElements.reduce(
          (sum, e) => sum + e.offsetHeight,
          0,
        );
        canvas.width = width;
        canvas.height = height;
        const ctx = canvas.getContext('2d');
        if (!ctx) {
          console.error('Could not create canvas context');
          return;
        }

        let y = 0;
        dataUrls.forEach(dataUrl => {
          const img = new Image();
          img.onload = () => {
            ctx.drawImage(img, 0, y);
            y += img.height;
          };
          img.src = dataUrl;
        });

        const link = document.createElement('a');
        link.download = `${generateFileStem(description)}.jpg`;
        link.href = canvas.toDataURL('image/jpeg', 0.95);
        link.click();
      })
      .catch(e => {
        console.error('Creating image failed', e);
      });
  };
}
