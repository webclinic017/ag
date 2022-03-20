import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import { AppContextProvider } from "./AppContext";
import Layout from "./components/Layout";
import Home from "./views/home";
import Positions from "./views/positions";

function App() {
	return (
		<AppContextProvider>
			<BrowserRouter>
				<Routes>
					<Route path="/" element={<Home />} />
					<Route path="/positions" element={<Positions />} />
				</Routes>
			</BrowserRouter>
		</AppContextProvider>
	);
}

export default App;
