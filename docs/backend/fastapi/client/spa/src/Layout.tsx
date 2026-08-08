import { Link, Outlet } from "react-router-dom";

export default function Layout() {
  return (
    <div className="app">
      <nav className="nav">
        <Link to="/">首页</Link>
        <Link to="/me">我的</Link>
      </nav>

      <main className="outlet">
        <Outlet />
      </main>
    </div>
  );
}
