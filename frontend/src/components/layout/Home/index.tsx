const HomeLyout = ({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) => {
    return (
        <div className="h-screen w-screen bg-cover bg-center bg-no-repeat bg-home flex justify-start items-center">
            {children}
        </div>
    );
};

export default HomeLyout;
