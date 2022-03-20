import { Drawer, List, ListItemButton, ListItemIcon, ListItemText, Toolbar } from "@mui/material";
import React, { FC } from "react";
import DashboardIcon from '@mui/icons-material/Dashboard';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import HistoryIcon from '@mui/icons-material/History';
import StackedBarChartIcon from '@mui/icons-material/StackedBarChart';
import AdbIcon from '@mui/icons-material/Adb';
import { useNavigate } from "react-router-dom";

const Sidebar:FC = () => {
    const navigate = useNavigate()
    return (
        <Drawer variant="permanent" sx={{width: 200, flexShrink: 0}} PaperProps={{sx: {width: 200, boxSizing: 'border-box'}}}>
            <Toolbar />
            <List sx={{pt: 3}}>
                <ListItemButton onClick={() => navigate('/')}>
                    <ListItemIcon>
                        <DashboardIcon color="inherit" />
                    </ListItemIcon>
                    <ListItemText primary="Overview" />
                </ListItemButton>
                <ListItemButton onClick={() => navigate('/positions')}>
                    <ListItemIcon>
                        <ShoppingCartIcon color="inherit" />
                    </ListItemIcon>
                    <ListItemText primary="Positions" />
                </ListItemButton>
                <ListItemButton>
                    <ListItemIcon>
                        <HistoryIcon color="inherit" />
                    </ListItemIcon>
                    <ListItemText primary="Trades" />
                </ListItemButton>
                <ListItemButton>
                    <ListItemIcon>
                        <StackedBarChartIcon color="inherit" />
                    </ListItemIcon>
                    <ListItemText primary="Reports" />
                </ListItemButton>
                <ListItemButton>
                    <ListItemIcon>
                        <AdbIcon color="inherit" />
                    </ListItemIcon>
                    <ListItemText primary="Agents" />
                </ListItemButton>
            </List>
        </Drawer>
    )
}

export default Sidebar