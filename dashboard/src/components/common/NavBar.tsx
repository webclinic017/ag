import {
	Circle,
	PauseCircle,
	PlayCircle,
	StopCircle,
} from "@mui/icons-material";
import {
	AppBar,
	Box,
	Button,
	Divider,
	Hidden,
	Stack,
	Toolbar,
	Typography,
} from "@mui/material";
import React, { FC, useCallback, useContext, useEffect } from "react";
import { Actions_Types, AppContext, Bot_Status } from "../../AppContext";
import API from "../../lib/api";

const NavBar: FC = ({}) => {
	const { state, dispatch } = useContext(AppContext);

	const onStartClick = useCallback(async () => {
		if (state.status == Bot_Status.ON) {
			return
		}
		try {
			await API.start()
			dispatch({
				type: Actions_Types.STATUS_CHANGED,
				payload: Bot_Status.ON
			})
		} catch (error) {
			console.error(error)
		}
	}, [state, dispatch])

	const onStopClick = useCallback(async () => {
		if (state.status == Bot_Status.OFF) {
			return
		}
		try {
			await API.stop()
			dispatch({
				type: Actions_Types.STATUS_CHANGED,
				payload: Bot_Status.OFF
			})
		} catch (error) {
			console.error(error)
		}
	}, [state, dispatch])

	return (
		<AppBar
			position="fixed"
			sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}>
			<Toolbar>
				<Typography variant="h6">AJ Bot</Typography>
				<Hidden xsDown>
                    <Box sx={{ml: 3}}>
					{state.status === Bot_Status.ON && (
						<Stack direction="row" spacing={1} alignItems="center">
							<Circle color="success" sx={{ fontSize: "12px" }} />
							<Typography variant="body1">Running</Typography>
						</Stack>
					)}
					{state.status === Bot_Status.OFF && (
						<Stack direction="row" spacing={1} alignItems="center">
							<Circle color="error" sx={{ fontSize: "12px" }} />
							<Typography variant="body1">Stopped</Typography>
						</Stack>
					)}
                    </Box>
				</Hidden>
				<Box sx={{ flexGrow: 1 }} />
				<Stack direction="row" spacing={1}>
					{state.status === Bot_Status.OFF && (
						<Button
							variant="contained"
							color="success"
							onClick={onStartClick}
							startIcon={<PlayCircle color="inherit" />}>
							Start
						</Button>
					)}
					{state.status == Bot_Status.ON && (
						<>
							<Button
								variant="contained"
								color="warning"
								startIcon={<PauseCircle color="inherit" />}>
								Pause
							</Button>
							<Button
								variant="contained"
								color="error"
								onClick={onStopClick}
								startIcon={<StopCircle color="inherit" />}>
								Stop
							</Button>
						</>
					)}
				</Stack>
			</Toolbar>
		</AppBar>
	);
};

export default NavBar;
