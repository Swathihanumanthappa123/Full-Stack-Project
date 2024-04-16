import app
from dao import DAO

def main():
    # Database connection details
    dbname = 'postgres'
    user = 'postgres'
    password = 'Swathi0616'
    host = '127.0.0.1'
    port = 5432

    # Initialize DAO with database connection details
    dao = DAO(dbname, user, password, host, port)

    # Example usage of DAO methods
    print("\n=== 10 Authors Ordered by Date of Birth ===")
    authors_ordered_by_dob = dao.get_authors_ordered_by_dob(limit=10)
    for author in authors_ordered_by_dob:
        print(f"{author.name} (DOB: {author.date_of_birth})")

    print("\n=== Total Sales for Author 'Lorelai Gilmore' ===")
    total_sales = dao.get_sales_total_for_author('Lorelai Gilmore')
    print(f"Total Sales: ${total_sales:.2f}")

    print("\n=== Top 10 Performing Authors by Sales Revenue ===")
    top_performing_authors = dao.get_top_performing_authors(limit=10)
    for rank, (author_name, total_revenue) in enumerate(top_performing_authors, start=1):
        print(f"{rank}. {author_name}: ${total_revenue:.2f}")

    # Close database connection
    dao.close_connection()

if __name__ == "__main__":
    main()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)