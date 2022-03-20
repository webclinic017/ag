import { styled } from "@mui/system";
import React, { FC } from "react";

const Div = styled('div')(({theme}) => (theme as any).mixins?.toolbar)

const AppBarSpacer:FC = () => <Div />

export default AppBarSpacer