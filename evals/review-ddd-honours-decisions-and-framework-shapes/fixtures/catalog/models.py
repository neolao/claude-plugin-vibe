from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    variants = relationship("Variant", back_populates="product", cascade="all, delete-orphan")

    def add_variant(self, sku: str, size: str) -> None:
        if any(v.sku == sku for v in self.variants):
            raise ValueError(f"variant {sku} already exists on product {self.id}")
        self.variants.append(Variant(sku=sku, size=size, product=self))


class Variant(Base):
    __tablename__ = "variants"

    sku = Column(String, primary_key=True)
    size = Column(String, nullable=False)
    product_id = Column(String, ForeignKey("products.id"), nullable=False)
    product = relationship("Product", back_populates="variants")
