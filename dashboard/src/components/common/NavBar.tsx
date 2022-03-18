import { AppBar, Box, Button, Stack, Toolbar, Typography } from "@mui/material";
import React,{ FC } from "react";

const NavBar:FC = ({}) => {

    return (
        <AppBar>
            <Toolbar>
                <Typography variant="h6">AJ Bot</Typography>
                <Box sx={{flexGrow: 1}} />
                <Stack direction="row" spacing={1}>
                    <Button>Stop</Button>
                </Stack>
            </Toolbar>
        </AppBar>
    )
}

export default NavBar