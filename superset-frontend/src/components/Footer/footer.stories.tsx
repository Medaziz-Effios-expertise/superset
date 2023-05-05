import React from "react";
import { Story, Meta } from '@storybook/react/types-6-0';
import Footer, { FooterProps } from './footer';

export default {
  title: 'Components/Footer',
  component: Footer,
} as Meta;

const Template: Story<FooterProps> = (args) => <Footer {...args} />;

export const Default = Template.bind({});
Default.args = {
  companyName: 'My Company',
};
