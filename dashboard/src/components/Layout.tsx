import { Toolbar } from "@mui/material";
import { Box, styled } from "@mui/system";
import React, { FC } from "react";
import AppBarSpacer from "./common/AppBarSpacer";
import NavBar from "./common/NavBar";
import Sidebar from "./common/Sidebar";

const Layout: FC = ({ children }) => (
	<Box sx={{ display: "flex" }}>
		<NavBar />
		<Sidebar />
		<Box component="main" sx={{ flexGrow: 1 }}>
            <Toolbar />
			{children}
		</Box>
	</Box>
);

export default Layout;
