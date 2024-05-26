#include <windows.h>
#include <shlobj.h>
#include <stdio.h>

#define IDC_BUTTON_CLEAN 101

LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

void CleanTempFiles() {
    TCHAR tempPath[MAX_PATH];
    
    if (GetTempPath(MAX_PATH, tempPath) != 0) {
        WIN32_FIND_DATA findFileData;
        HANDLE hFind = FindFirstFile(tempPath, &findFileData);

        if (hFind != INVALID_HANDLE_VALUE) {
            do {
                if (!(findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)) {
                    TCHAR filePath[MAX_PATH];
                    _stprintf(filePath, _T("%s%s"), tempPath, findFileData.cFileName);
                    DeleteFile(filePath);
                }
            } while (FindNextFile(hFind, &findFileData) != 0);
            FindClose(hFind);
        }
    }
}

int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PWSTR pCmdLine, int nCmdShow) {
    const wchar_t CLASS_NAME[] = L"TempFileCleaner";
    
    WNDCLASS wc = { 0 };
    
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = CLASS_NAME;
    wc.hCursor = LoadCursor(NULL, IDC_ARROW);

    RegisterClass(&wc);

    HWND hwnd = CreateWindowEx(
        0,
        CLASS_NAME,
        L"Temporary File Cleaner",
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT, 300, 150,
        NULL,
        NULL,
        hInstance,
        NULL
    );

    if (hwnd == NULL) {
        return 0;
    }

    ShowWindow(hwnd, nCmdShow);

    MSG msg = { 0 };
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}

LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    switch (uMsg) {
        case WM_CREATE:
            CreateWindow(
                L"BUTTON", 
                L"Clean Temp Files", 
                WS_TABSTOP | WS_VISIBLE | WS_CHILD | BS_DEFPUSHBUTTON, 
                50, 
                50, 
                200, 
                30, 
                hwnd, 
                (HMENU)IDC_BUTTON_CLEAN, 
                (HINSTANCE)GetWindowLongPtr(hwnd, GWLP_HINSTANCE), 
                NULL);
            break;
        case WM_COMMAND:
            if (LOWORD(wParam) == IDC_BUTTON_CLEAN) {
                CleanTempFiles();
                MessageBox(hwnd, L"Temporary files cleaned!", L"Success", MB_OK);
            }
            break;
        case WM_DESTROY:
            PostQuitMessage(0);
            return 0;
        default:
            return DefWindowProc(hwnd, uMsg, wParam, lParam);
    }
    return TRUE;
}
