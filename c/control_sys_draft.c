switch(check_sys_status()) {
    case 0:
        return_to_start(); break;
    case 1:
        go_with_status(1); break;
    case 2:
        go_with_status(2); break;
    default:
        unexpected_handle();
}
