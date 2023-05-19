/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

import React, { useCallback } from 'react';
import { css, t, styled } from '@superset-ui/core';
import { Tooltip } from 'src/components/Tooltip';
import { useComponentDidMount } from 'src/hooks/useComponentDidMount';
import Icons from 'src/components/Icons';


const StyledLink = styled.a`
  ${({ theme }) => css`
    font-size: ${theme.typography.sizes.xl}px;
    display: flex;
    padding: 0 0 0 ${theme.gridUnit * 2}px;
  `};
`;

export interface CheckboxApiComponentProps {
  id: number;
  isChecked?: boolean;
  showTooltip?: boolean;
  saveCheckboxApi(id: number): void;
  fetchCheckboxApi: () => void;
  defaultChecked?: boolean;
}

const CheckboxApiComponent = ({
  id,
  isChecked,
  showTooltip,
  saveCheckboxApi,
  fetchCheckboxApi,
  defaultChecked,
}: CheckboxApiComponentProps) => {
  useComponentDidMount(() => { });

  const onClick = useCallback(
    async (e: React.MouseEvent) => {
      e.preventDefault();
      await saveCheckboxApi(id);
      await fetchCheckboxApi();
    },
    [id, saveCheckboxApi, fetchCheckboxApi]
  );

  const content = (
    <StyledLink
      href="#"
      onClick={onClick}
      className="set-home-dashboard"
      data-test="set-home-dashboard"
      role="button"
      defaultChecked={defaultChecked}
    >
      {isChecked ? <Icons.IconHome /> : <Icons.IconHomeUnselected />}
    </StyledLink>
  );

  if (showTooltip) {
    return (
      <Tooltip
        id="set-home-dashboard-tooltip"
        title={t('Click to select/deselect Home dashboard')}
      >
        {content}
      </Tooltip>
    );
  }

  return content;
};
export default CheckboxApiComponent;
